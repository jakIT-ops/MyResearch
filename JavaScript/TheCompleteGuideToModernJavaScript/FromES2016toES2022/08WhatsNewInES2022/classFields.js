class ButtonToggle extends HTMLElement {
    constructor(){
        super();
        // public field
        this.color = 'green'
        // private field
        this._value = true;
    }

    toggle(){
        this.value = !this.value
    }
}

const button = new ButtonToggle();
console.log(button.color);
// green - public fields are accessible from outside classes

button._value = false;
console.log(button._value);
// false - no error thrown, we can access it from outside the class
