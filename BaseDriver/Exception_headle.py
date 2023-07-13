import time


def exception_retry(max_times=3, wait_seconds=0.1):
    # decorator wrapper 不变
    def decorator(func):
        def wrapper(*args, **kwargs):
            basedriver = args[0]  # 第一个参数是 BaseDriver 实例
            retries = 0
            while retries < max_times:
                try:
                    # 运行的func方法 find click()
                    result = func(*args, **kwargs)
                    basedriver.driver.implicitly_wait(10)
                    return result
                except Exception as e:
                    # 异常截图
                    basedriver.driver.save_screenshot('./imgs/Exception_Img/123.png')
                    # 获取当前的page页面 self.driver.page_source
                    retries += 1
                    # 0.2s
                    time.sleep(wait_seconds)
                    return func(*args, **kwargs)
            # 超过3次之后异常
            raise Exception(f"Max retries reached for function {func.__name__}")

        return wrapper

    return decorator
