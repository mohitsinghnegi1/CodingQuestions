class SingletonClass {
    static instance: SingletonClass = new SingletonClass;
    private constructor() {

    }
    static getInstance() {
        return this.instance;
    }
}

console.log(SingletonClass.getInstance());