from base.execution_engine import ExecutionEngine
from human import Human
from field import Field
import time
from multiprocessing import Pool
from rx import create

if __name__ == "__main__":
    agent_list = []
    env_list = []

    jaiyun = Human("jaiyun", 36.7, "arctic clothes")
    spring = Field("spring", 20)
    
    engine = ExecutionEngine(5)
    engine.append_bootloader("spring", "./bootloader/spring.simx")

    engine.state = "spring"
    engine.set_agent_source(jaiyun.get_source())
    engine.set_env_source(spring.get_source())

    engine.run_boot_loader()
    
    #병렬 실행 적용
    start_time = time.time()
    for i in range(10) : 
        engine.run_multi_parts()
    end_time = time.time()
    execution_time = end_time - start_time
    print("병렬 실행 시간: {}초".format(execution_time))
    