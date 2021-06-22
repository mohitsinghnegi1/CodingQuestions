
interface IpaymentGateway {
    pay(amountInRs: number, paymentDetails: IpaymentDetails): void; // This is a must function which will be used by Store
}

interface IUser {
    name: string;
    emailId?: string;
    phoneNo?: number;
}

interface IpaymentDetails {
    getUser(): IUser;
    debitAmount(amout: number): boolean;
}

class Store {
    paymentGateWayProcessor: IpaymentGateway;
    constructor(paymentGateWayProcessor: IpaymentGateway) {
        this.paymentGateWayProcessor = paymentGateWayProcessor;
    }

    buyHelmet(quantity: number, paymentDetails: IpaymentDetails) {
        let helmentPriceInRs = 100;
        this.paymentGateWayProcessor.pay(helmentPriceInRs * quantity, paymentDetails);
    }

    buyShoes(quantity: number, paymentDetails: IpaymentDetails) {
        let shoesPrice = 200;
        this.paymentGateWayProcessor.pay(shoesPrice * quantity, paymentDetails);
    }
}



class GPay {
    constructor() { }
    makePayment(amount: number, paymentDetails: IpaymentDetails) {
        paymentDetails.debitAmount(amount);
        console.log(`${ paymentDetails.getUser().name } has successfull made payment of rs ${ amount } through GPay`);
    }
}

// lets create a gpayProcessor

class GPayProcessor implements IpaymentGateway {
    gpay: GPay;
    constructor() {
        this.gpay = new GPay();
    }
    pay(amountInRs: number, paymentDetails: IpaymentDetails): void {
        this.gpay.makePayment(amountInRs, paymentDetails);
    }

}

class PhonePay {
    constructor() { }
    payAmount(amount: number, paymentDetails: IpaymentDetails) {
        paymentDetails.debitAmount(amount);
        console.log(`${ paymentDetails.getUser().name } has successfull made payment of rs ${ amount } through PhonePay`);
    }
}

class PhonePayProcessor implements IpaymentGateway {
    phonePay: PhonePay;
    constructor() {
        this.phonePay = new PhonePay();
    }
    pay(amountInRs: number, paymentDetails: IpaymentDetails): void {
        this.phonePay.payAmount(amountInRs, paymentDetails);
    }
}

class _User implements IUser {
    name: string;
    email: string | undefined;
    phoneNo: number | undefined;
    constructor(name: string, email?: string, phoneNo?: number) {
        this.name = name;
        this.email = email;
        this.phoneNo = phoneNo;
    }
}
class paymentDetails implements IpaymentDetails {
    balance: number;
    user: IUser;

    constructor(user: IUser, balance: number) {
        this.user = user;
        this.balance = balance;
    }
    getUser(): IUser {
        return this.user;
    }
    debitAmount(amout: number): boolean {
        if (amout > this.balance) return false;
        this.balance = this.balance - amout;
        return true;
    }

}

let store = new Store(new GPayProcessor());
store.buyHelmet(10, new paymentDetails(new _User('Mohit'), 20000));
store.buyShoes(10, new paymentDetails(new _User('Vaibhav'), 20000));


let store2 = new Store(new PhonePayProcessor());
store2.buyHelmet(10, new paymentDetails(new _User('Guru'), 20000));
store2.buyShoes(10, new paymentDetails(new _User('Harshit'), 20000));