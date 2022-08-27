interface Animal {
    name: string;
    sound: string;
}
interface Human {
    name: string;
    nickname: string;
}

type LivingThing = Extract<keyof Animal, keyof Human>;
function sayMyName(who: Record<LivingThing, string>): void {
    console.log(who.name);
}
const animal: Animal = { name: "Lion", sound: "Rawwwhhh" };
const human: Human = { name: "Jacob", nickname: "Jaco-bee" };
sayMyName(animal);
sayMyName(human);
