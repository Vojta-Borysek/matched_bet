from scheduler import MainClass
import schedule
import time


def step2():
    # Create an instance of MainClass
    main_instance = MainClass()

    # Execute the method immediately
    main_instance.run()

    # Schedule the job to run every 10 minutes
    schedule.every(10).minutes.do(main_instance.run)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    # step1() 
    step2()
