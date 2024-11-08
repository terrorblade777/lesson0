rurik_dynasty={"Rurik":879 , "Oleg":912 , "Igor":945 , "Olga":969}
print(rurik_dynasty)
print(rurik_dynasty["Oleg"])
print(rurik_dynasty.get("Svyatoslav"))
rurik_dynasty.update({"Vladimir":1015 , "Yaroslav":1054})
a = rurik_dynasty.pop("Rurik")
print(rurik_dynasty)
print(a)




my_set={1, 2, 6, "Kikimara", 6, 2, 1., "Kikimara"}
print(my_set)
my_set.update([7, 5,"Bolotnaya", 3, 4])
print(my_set)
my_set.discard(3)
print(my_set)




