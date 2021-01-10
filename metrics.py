#!usr/bin/env python3

import psutil
import sys

metrics = sys.argv[1]
if metrics == 'mem':
    memory = psutil.virtual_memory()
    mem_total = f'{memory.total}'
    mem_used = f'{memory.used}'
    mem_free = f'{memory.free}'
    mem_shared = f'{memory.shared}'
    swap = psutil.swap_memory()
    mem_swap_total = f'{swap.total}'
    mem_swap_used = f'{swap.used}'
    mem_swap_free = f'{swap.free}'
    print(
        "virtual total " + mem_total,
        "\nvirtual used " + mem_used,
        "\nvirtual free " + mem_free,
        "\nvirtual shared " + mem_shared
    )
    print(
        "swap total " + mem_swap_total,
        "\nswap used " + mem_swap_used,
        "\nswap free " + mem_swap_free
    )
elif metrics == 'cpu':
    getting_cpu_value = psutil.cpu_times()
    cpu_idle = f'{getting_cpu_value.idle}'
    cpu_user = f'{getting_cpu_value.user}'
    cpu_guest = f'{getting_cpu_value.guest}'
    cpu_iowait = f'{getting_cpu_value.iowait}'
    cpu_stolen = f'{getting_cpu_value.steal}'
    cpu_system = f'{getting_cpu_value.system}'
    print(
        "system.cpu.idle " + cpu_idle,
        "\nsystem.cpu.user " + cpu_user,
        "\nsystem.cpu.guest " + cpu_guest,
        "\nsystem.cpu.iowait " + cpu_iowait,
        "\nsystem.cpu.stolen " + cpu_stolen,
        "\nsystem.cpu.system " + cpu_system
    )
else:
    print("Wrong input! Use only mem or cpu")
