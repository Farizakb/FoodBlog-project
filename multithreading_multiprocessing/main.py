import threading,random
import time 
import requests

def do_something():
    res = requests.get('https://picsum.photos/200')
    with open(f'./images/image_{random.randint(0,100000)}.png', 'wb') as f:
        f.write(res.content)

t1 = time.time()
threads = []
for _ in range(100):
    thread = threading.Thread(target=do_something)
    thread.start()
    print("start")
    threads.append(thread)
    
for th in threads:
    th.join()
    print("stop")

t2 = time.time()
time_delta = t2 - t1

print(time_delta)


# if __name__ == '__main__':
#     t1 = time.time()
#     proccesses = []
#     for _ in range(100):
#         proccess = multiprocessing.Process(target=download_image)
#         proccess.start()
#         proccesses.append(proccess)


#     for pr in proccesses:
#         pr.join()

#     t2 = time.time()

    # delta_time = t2 - t1

    # print('delta_time', delta_time)

