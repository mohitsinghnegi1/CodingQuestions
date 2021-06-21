// Command pattern has the ability to execute an expression and undo the result
interface ICommand {
    prevValue: number;
    no: number;
    nextValue: number;
    exec(prevVal: number): number;
    undo(): number;
}

class Addition implements ICommand {
    prevValue: number;
    nextValue: number;
    no: number;

    constructor(no: number) {
        this.prevValue = 0;
        this.nextValue = 0;
        this.no = no;
    }
    exec(curVal: number): number {
        this.prevValue = curVal;
        this.nextValue = curVal + this.no;
        return this.nextValue;
    }
    undo(): number {
        this.nextValue = this.prevValue;
        this.prevValue = 0;
        return this.nextValue;
    }

}

class Substraction implements ICommand {
    prevValue: number;
    nextValue: number;
    no: number;

    constructor(no: number) {
        this.prevValue = 0;
        this.nextValue = 0;
        this.no = no;
    }
    exec(curVal: number): number {
        this.prevValue = curVal;
        this.nextValue = curVal - this.no;
        return this.nextValue;
    }
    undo(): number {
        this.nextValue = this.prevValue;
        this.prevValue = 0;
        return this.nextValue;
    }
}

class Multiplication implements ICommand {
    prevValue: number;
    nextValue: number;
    no: number;

    constructor(no: number) {
        this.prevValue = 0;
        this.nextValue = 0;
        this.no = no;
    }
    exec(curVal: number): number {
        this.prevValue = curVal;
        this.nextValue = curVal * this.no;
        return this.nextValue;
    }
    undo(): number {
        this.nextValue = this.prevValue;
        this.prevValue = 0;
        return this.nextValue;
    }
}

class Division implements ICommand {
    prevValue: number;
    nextValue: number;
    no: number;

    constructor(no: number) {
        this.prevValue = 0;
        this.nextValue = 0;
        this.no = no;
    }
    exec(curVal: number): number {
        this.prevValue = curVal;
        this.nextValue = curVal / this.no;
        return this.nextValue;
    }
    undo(): number {
        this.nextValue = this.prevValue;
        this.prevValue = 0;
        return this.nextValue;
    }
}

class AdditionThenMultiplication implements ICommand {
    prevValue: number;
    nextValue: number;
    no: number;
    no2: number;

    constructor(no: number, no2: number) {
        this.prevValue = 0;
        this.nextValue = 0;
        this.no = no;
        this.no2 = no2;
    }
    exec(curVal: number): number {
        this.prevValue = curVal;
        this.nextValue = new Addition(this.no).exec(curVal); // these two commands will be considered as atomic
        console.log('after add ', this.nextValue);
        this.nextValue = new Multiplication(this.no2).exec(this.nextValue);
        console.log('after mul ', this.nextValue);
        return this.nextValue;
    }
    undo(): number {
        this.nextValue = this.prevValue;
        this.prevValue = 0;
        return this.nextValue;
    }
}

class Calculator {
    private value: number;
    private history: ICommand[];
    constructor() {
        this.value = 0;
        this.history = [];
    }

    executeCommand(command: ICommand) {
        this.value = command.exec(this.value);
        this.history.push(command);
        return this.value;
    }

    undo() {
        if (this.history.length) {
            let command: ICommand | undefined = this.history.pop();
            let val = command?.undo();
            console.log('val', val);
            if (val != null) this.value = val;
        }
        return this.value;
    }
}

let calculator = new Calculator();

let val = calculator.executeCommand(new Addition(10));
console.log(`current val ${ val }`);
val = calculator.executeCommand(new Addition(20));//
console.log(`current val ${ val }`);
val = calculator.executeCommand(new Addition(30));//
console.log(`current val ${ val }`);

val = calculator.undo();
console.log(`undo val  ${ val }`);
val = calculator.undo();
console.log(`undo val  ${ val }`);

val = calculator.executeCommand(new Substraction(30));
console.log(`current val ${ val }`);
val = calculator.executeCommand(new Addition(50));
console.log(`current val ${ val }`);
// val = calculator.undo();
// console.log(`undo val  ${ val }`);
// val = calculator.undo();
// console.log(`undo val  ${ val }`);


val = calculator.executeCommand(new Multiplication(30));
console.log(`current val ${ val }`);
val = calculator.executeCommand(new Multiplication(10));
console.log(`current val ${ val }`);
val = calculator.undo();
console.log(`undo val  ${ val }`);
val = calculator.undo();
console.log(`undo val  ${ val }`);
val = calculator.undo();
console.log(`undo val last  ${ val }`);
// val = calculator.undo();
// console.log(`undo val  ${ val }`);
val = calculator.executeCommand(new AdditionThenMultiplication(10, 20));
console.log(`current val ${ val }`);

val = calculator.undo();
console.log(`undo val last  ${ val }`);