from .components.time_based_event import TimedBasedEvent

def task3():
    print("han pasado 3 segundos")

def task2():
    print("han pasado 2 segundos")

def task1():
    print("ha pasado 1 segundo")

def main():
    task3seconds = TimeBasedEvents(task3, 3, enabled = True)
    task2seconds = TimeBasedEvents(task2, 2, enabled = True)
    task1seconds = TimeBasedEvents(task1, 1, enabled = True)
    while(True):
        task3seconds.update()
        task2seconds.update()
        task1seconds.update()

if __name__ == "__main__":
    main()