//console.log(subscription)
console.log(subscription.devices_number)
//console.log({{subscription.duration}})


 //function getSubscriptionData() {
//    let subscription = {
//        "pkid": 0,
//        "user": "string",
//        "user_data": {
//            "user_id": -9223372036854776000,
//            "user_name": "string",
//            "first_name": "string",
//            "last_name": "string",
//            "is_bot_blocked": true
//        },
//        "tariff": 0,
//        "tariff_data": {
//            "pkid": 0,
//            "duration": 0,
//            "duration_data": {
//            "pkid": 0,
//            "month_duration": 12,
//            "currency": "string",
//            "amount": "string"
//            },
//            "devices_number": 5,
//            "operation": "equal",
//            "discount_percentage": 20,
//            "total_discount": "25",
//            "initial_price": "5000",
//            "discounted_price": "4000",
//            "curency": "RUB"
//        },
//        "total_price": "string",
//        "discount": "string",
//        "status": "paid",
//        "vpn_items": [
//            {
//            "pkid": 0,
//            "protocol": 0,
//            "instance": 0
//            }
//        ]
//    }


//       return subscription;
//    }
//   getSubscriptionData()
let tg = window.Telegram.WebApp
console.log(tg)
const params = new URLSearchParams(window.location.search)
const month_duration = params.get('month_duration')
for (const param of params) {
  console.log(param)
}


function createDivElement(month_duration){

        let mainDiv = document.createElement('div')
        mainDiv.classList.add('mainDivStyle')
        var mainEl = document.querySelector('.mainClass')
        mainEl.prepend(mainDiv)

        let pageDiv = document.createElement('div')
        pageDiv.classList.add('pageDivStyle')
        mainDiv.prepend(pageDiv)
        pageDiv.innerHTML = "<p>" + 'Доступ к VPN на ' + month_duration + ' мес.' + "</p>"

        let plashTariffDiv = document.createElement('div')
        plashTariffDiv.classList.add('plashTariffDivStyle')
        mainDiv.append(plashTariffDiv)
}
createDivElement(subscription.duration)

function createPlashTariffElement(discounted_price, duration_loc, curency, devices_number, devices_loc, discount_percentage, month_duration){

        let newPlashTariffDiv = document.querySelector('.plashTariffDivStyle')

        let plashPriceTariffDiv = document.createElement('div')
        plashPriceTariffDiv.classList.add('plashPriceTariffDivStyle')
        newPlashTariffDiv.prepend(plashPriceTariffDiv)
        plashPriceTariffDiv.innerText = discounted_price + ' ' + curency;
        
        let plashDevicesTariffDiv = document.createElement('div')
        plashDevicesTariffDiv.classList.add('plashDevicesTariffDivStyle')
        plashPriceTariffDiv.after(plashDevicesTariffDiv)
        plashDevicesTariffDiv.innerText = devices_number + ' ' + devices_loc;

        let plashDiscontTariffDiv = document.createElement('div')
        plashDiscontTariffDiv.classList.add('plashDiscountTariffDivStyle')
        plashPriceTariffDiv.after(plashDiscontTariffDiv)
        plashDiscontTariffDiv.innerText = discount_percentage + '%*';

        let plashMonthTariffDiv = document.createElement('div')
        plashMonthTariffDiv.classList.add('plashMonthTariffDivStyle')
        newPlashTariffDiv.append(plashMonthTariffDiv)
        plashMonthTariffDiv.innerHTML = month_duration

        let plashMonthTextTariffDiv = document.createElement('div')
        plashMonthTextTariffDiv.classList.add('plashMonthTextTariffDivStyle')
        plashMonthTariffDiv.after(plashMonthTextTariffDiv)
        plashMonthTextTariffDiv.innerHTML = '<p>'+ duration_loc + ' подписки на VPN' + '</p>'

}
createPlashTariffElement(subscription.price,
    subscription.duration_loc, subscription.currency,
    subscription.devices_number, subscription.devices_loc,
    subscription.discount, subscription.duration)

function createCheckBox(){

let newMainDiv = document.querySelector('.mainDivStyle')

        var checkbox = document.createElement('input');
        checkbox.classList.add('checkboxTariffStyle')

        checkbox.type = "checkbox";
        checkbox.name = "name";
        checkbox.value = "value";
        checkbox.id = "id";

        var label = document.createElement('label')
        label.classList.add('labelTariffStyle')
        label.htmlFor = "id";
        label.appendChild(document.createTextNode('Я согласен(на) с условиями оферты рекуррентных платежей и политики обработки персональных данных*'));

        newMainDiv.append(checkbox);
        checkbox.after(label);
}

createCheckBox()

function createTariffPayButton(){

    let newLabel = document.querySelector('.labelTariffStyle')
    let newCheckBox = document.querySelector('.checkboxTariffStyle')

        let buttonTatiffPay = document.createElement('div')
        buttonTatiffPay.classList.add('buttonTatiffPaySty')
        newLabel.after( buttonTatiffPay)
        buttonTatiffPay.innerHTML = '<p>' + "Оплатить" + '</p>'
    

        var i = 0;

        newCheckBox.onclick = function(){
      
       i++

       if(i % 2 != 0){
        
        buttonTatiffPay.style.backgroundColor = "rgb(116, 138, 212)"

       }
       else{
        buttonTatiffPay.style.backgroundColor = "rgb(174, 190, 243)"
       }
       
       console.log(i)
       
     }
}
createTariffPayButton()
