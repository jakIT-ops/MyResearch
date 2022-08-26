// method defined outside of the class body
let initVal;

class ButtonToggle{
    #value = false;

    get getValue(){
        if(!this.#value){
            throw new Error('no value');
        } 
        return this.#value
    }

    static {
        initVal = () => {
            this.#value = this.getValue;
        }
    }
}

initVal();
