import sys
import wikipediaapi
from collections import deque
import time


class NotFoundPage(RuntimeError):
    pass


def build_tree(start_page, target_page):
    wiki_api = wikipediaapi.Wikipedia('en')
    start_page = wiki_api.page(start_page)
    target_page = wiki_api.page(target_page)
    tree = {}
    visited = set()
    queue = deque()
    queue.append(start_page)
    while len(queue):
        current_page = queue.popleft()
        all_links = current_page.links
        if target_page.title in all_links:
            tree[target_page.title] = current_page.title
            return tree
        for link in all_links.values():
            if link.title not in visited:
                tree[link.title] = current_page.title
                if link == target_page:
                    return tree
                visited.add(link.title)
                queue.append(link)
    raise NotFoundPage


def build_bridge(start_page, target_page):
    tree = build_tree(start_page, target_page)
    current_page, bridge = target_page, [target_page]
    while current_page != start_page:
        bridge.append(tree[current_page])
        current_page = tree[current_page]
    return bridge[::-1]


if __name__ == '__main__':
    argv = sys.argv[1:]
    if (len(argv) != 2):
        raise ValueError('Not enough arguments')
    start, target = argv[0], argv[1]
    time_start = time.time()
    bridge = build_bridge(start, target)
    for page in bridge:
        print(page)
    taken_time = int(time.time() - time_start)
    print(f'It takes {taken_time // 60} minutes and {taken_time % 60} seconds')