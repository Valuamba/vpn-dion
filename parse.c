static char *bytes(uint64_t b)
  static const char *COMMAND_NAME;
  static void show_usage(void)
  {
 -       fprintf(stderr, "Usage: %s %s { <interface> | all | interfaces }
 [public-key | private-key | listen-port | fwmark | peers | preshared-keys |
 endpoints | allowed-ips | latest-handshakes | transfer |
 persistent-keepalive | dump]\n", PROG_NAME, COMMAND_NAME);
 
 +       fprintf(stderr, "Usage: %s %s { <interface> | all | interfaces }
 [public-key | private-key | listen-port | fwmark | peers | preshared-keys |
 endpoints | allowed-ips | latest-handshakes | transfer |
 persistent-keepalive | dump | json]\n", PROG_NAME, COMMAND_NAME);
 +}
 +
 +static void json_print(struct wgdevice *device)
 +{
 +       struct wgpeer *peer;
 +       struct wgallowedip *allowedip;
 +       terminal_printf(TERMINAL_RESET);
 +       terminal_printf("  {\n");
 +       terminal_printf("    \"interface\": \"%s\",\n", device->name);
 +       terminal_printf("    \"public_key\": \"%s\",\n",
 key(device->public_key));
 +       terminal_printf("    \"private_key\": \"%s\",\n",
 key(device->private_key));
 +       terminal_printf("    \"port\": \"%d\",\n", device->listen_port);
 +       if (device->fwmark)
 +               terminal_printf("    \"fwmark\": \"0x%x\",\n",
 device->fwmark);
 +       else
 +               terminal_printf("    \"fwmark\": null,\n");
 +       terminal_printf("    \"peers\": [\n");
 +       sort_peers(device);
 +       for_each_wgpeer(device, peer) {
 +               terminal_printf("       {\n");
 +               terminal_printf("         \"peer\": \"%s\",\n",
 key(peer->public_key));
 +               if (peer->flags & WGPEER_HAS_PRESHARED_KEY)
 +                       terminal_printf("         \"preshared_key\":
 \"%s\",\n", key(peer->preshared_key));
 +               else
 +                       terminal_printf("         \"preshared_key\":
 null,\n");
 +               if (peer->endpoint.addr.sa_family == AF_INET ||
 peer->endpoint.addr.sa_family == AF_INET6)
 +                       terminal_printf("         \"endpoint\":
 \"%s\",\n", endpoint(&peer->endpoint.addr));
 +               else
 +                       terminal_printf("         \"endpoint\": null,\n");
 +               terminal_printf("         \"allowed_ips\": [\n");
 +               if (peer->first_allowedip) {
 +                       terminal_printf("           ");
 +                       for_each_wgallowedip(peer, allowedip)
 +                               terminal_printf("\"%s/%u\"%s",
 ip(allowedip), allowedip->cidr, allowedip->next_allowedip ? ", " : "\n");
 +               }
 +               terminal_printf("         ],\n");
 +               if (peer->last_handshake_time.tv_sec)
 +                       terminal_printf("         \"latest_handshake\":
 %ld,\n", peer->last_handshake_time.tv_sec);
 +               else
 +                       terminal_printf("         \"latest_handshake\":
 null,\n");
 +               terminal_printf("         \"transfer\": {\n");
 +               terminal_printf("          \"received\": %ld,\n",
 peer->rx_bytes);
 +               terminal_printf("          \"sent\": %ld\n",
 peer->tx_bytes);
 +               terminal_printf("         },\n");
 +               if (peer->persistent_keepalive_interval)
 +                       terminal_printf("
  \"persistent_keepalive\": %d\n", peer->persistent_keepalive_interval);
 +               else
 +                       terminal_printf("
  \"persistent_keepalive\": null\n");
 +               if (peer->next_peer)
 +                       terminal_printf("       },\n");
 +               else
 +                       terminal_printf("       }\n");
 +       }
 +       terminal_printf("    ]\n");
 +       terminal_printf("  }");
  }

  static void pretty_print(struct wgdevice *device)
 @@ -396,6 +451,8 @@ int show_main(int argc, char *argv[])
                 }
                 ret = !!*interfaces;
                 interface = interfaces;
 +               if (argc == 3 && !strcmp(argv[2], "json"))
 +                       terminal_printf("[\n");
                 for (size_t len = 0; (len = strlen(interface)); interface
 += len + 1) {
                         struct wgdevice *device = NULL;

 @@ -404,7 +461,13 @@ int show_main(int argc, char *argv[])
                                 continue;
                         }
                         if (argc == 3) {
 -                               if (!ugly_print(device, argv[2], true)) {
 +                               if (!strcmp(argv[2], "json")) {
 +                                       json_print(device);
 +                                       if (strlen(interface + len + 1))
 +                                               terminal_printf(",\n");
 +                                       else
 +                                               terminal_printf("\n");
 +                               } else if (!ugly_print(device, argv[2],
 true)) {
                                         ret = 1;
                                         free_wgdevice(device);
                                         break;
 @@ -417,6 +480,8 @@ int show_main(int argc, char *argv[])
                         free_wgdevice(device);
                         ret = 0;
                 }
 +               if (argc == 3 && !strcmp(argv[2], "json"))
 +                       terminal_printf("]\n");
                 free(interfaces);
         } else if (!strcmp(argv[1], "interfaces")) {
                 char *interfaces, *interface;
 @@ -444,7 +509,11 @@ int show_main(int argc, char *argv[])
                         return 1;
                 }
                 if (argc == 3) {
 -                       if (!ugly_print(device, argv[2], false))
 +                       if (!strcmp(argv[2], "json")) {
 +                               terminal_printf("[\n");
 +                               json_print(device);
 +                               terminal_printf("\n]\n");
 +                       } else if (!ugly_print(device, argv[2], false))
                                 ret = 1;
                 } else
                         pretty_print(device);