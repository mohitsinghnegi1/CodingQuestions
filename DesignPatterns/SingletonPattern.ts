class SingletonClass {
    static instance: SingletonClass = new SingletonClass;
    private constructor() {

    }
    static getInstance() {
        return this.instance;
    }
}

console.log(SingletonClass.getInstance());



class FancyLogger {
    static instance: FancyLogger;
    logs: string[] = [];
    constructor() {
        if (FancyLogger.instance == null) {
            FancyLogger.instance = this;
        }
        return FancyLogger.instance;
    }

    printLogs() {
        console.log("log count ", this.logs);
    }

    printLogCount() {
        console.log(this.logs.length);
    }

    pushLog(log: string) {
        this.logs.push(log);
    }

}

let logger = new FancyLogger();
Object.freeze(logger);

logger.pushLog('mohit');
logger.pushLog('singh');
logger.printLogs();
logger.printLogCount();

logger = new FancyLogger();

logger.pushLog('mohit2');
logger.pushLog('singh1');
logger.printLogs();
logger.printLogCount();

