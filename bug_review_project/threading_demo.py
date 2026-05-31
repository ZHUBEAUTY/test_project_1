import threading

counter = 0


def increase():
    global counter

    for _ in range(100000):
        # 竞态条件
        counter += 1


threads = []

for i in range(5):
    t = threading.Thread(target=increase)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(counter)