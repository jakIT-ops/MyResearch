const family = new Map();

family.set("Dad", 40);
family.set("Mom", 50);
family.set("Son", 20);

family;
// Map { Dad → 40, Mom → 50, Son → 20 }
family.size;
// 3

family.forEach((val,key) => console.log(key,val));
// Dad 40
// Mom 50
// Son 20

for(const [key,val] of family){
  console.log(key,val);
}
// Dad 40
// Mom 50
// Son 20
