# GLENN GUDMUNSON multiplication table
print("\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12")
for i in range(1,13):
    print(f"\n{i}", end="")
    for x in range(1,13):
        print(f"\t{x*i}", end="")


