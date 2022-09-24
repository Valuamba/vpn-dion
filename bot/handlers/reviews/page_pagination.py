# https://www.zacfukuda.com/blog/pagination-algorithm


def paginate(current, max):
    if not current or not max:
        return None

    prev = None if current == 1 else current - 1
    next = None if current == max else current + 1
    items = [{ '1': 1}]

    if current == 1 and max == 1:
        return current, prev, next, items

    if current > 4: items.append('...')

    r = 2 if current == 1 or current == max else 1
    r1 = current - r
    r2 = current + r

    start_from = r1 if r1 > 2 else 2
    for i in range(start_from, min(max, r2)):
        items.append(i)

    if r2 + 1 < max:
        items.append('...')

    if r2 < max:
        items.append(max)


    return current, prev, next, items


current, prev, next, items = paginate(6, 10)

print(current)
print(prev)
print(next)
print(items)


# class PagePaginationMetadata:
#     pass
#
#
# # def getrows_byslice(seq, rowlen):
# #     for start in xrange(0, len(seq), rowlen):
# #         yield seq[start:start+rowlen]
#
# # 1 2 3 4 5 >>
# # << 3 4  5 6 7 >>
# # << 5 6 7 8 9
#
# arr = []
# for i in range(10):
#     arr.append(i)
#
#
# def calculate_pagination_metadata(items: [], selected_page=0):
#     max_page = 5
#     selected_items = items[selected_page:selected_page + 1]
#
#
# class Solution:
#     def solve(self, book, page, page_size):
#         l = page * page_size
#         return book[l:l + page_size]
#
#
# ob = Solution()
#
# book = ["hello", "world", "programming", "language", "python", "c++",
#         "java"]
# page = 1
# page_size = 1
# print(ob.solve(book, page, page_size))
