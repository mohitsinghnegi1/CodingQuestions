interface PhoneInterface {
    description: string;
    getDescription(): string;
    getCost(): number;
}

abstract class BasePhone implements PhoneInterface {
    abstract description: string;
    getDescription(): string {
        return this.description;
    }
    abstract getCost(): number;

}

class IPhone extends BasePhone {
    description: string = "Brand new Iphone";
    getCost(): number {
        return 80000;
    }

}

class AndroidPhone extends BasePhone {
    description: string = "Brand new Android Phone";
    getCost(): number {
        return 20000;
    }

}

abstract class PhoneOption extends BasePhone {

    abstract decoratedPhone: BasePhone;
    abstract getCost(): number;
}

class PhoneWithMemoryCard extends PhoneOption {
    description: string;

    decoratedPhone: BasePhone;

    hasMemoryCard: boolean;

    constructor(phone: BasePhone) {
        super();
        this.decoratedPhone = phone;
        this.description = this.decoratedPhone.getDescription() + ', With Memory Card';
        this.hasMemoryCard = true;
    }

    getCost(): number {
        return this.decoratedPhone.getCost() + 800;
    }



}

class PhoneWithTemporGlass extends PhoneOption {

    decoratedPhone: BasePhone;
    description: string;

    hasTemporGlass: boolean;

    constructor(phone: BasePhone) {
        super();
        this.decoratedPhone = phone;
        this.description = this.decoratedPhone.getDescription() + ', With Tempor Glass';
        this.hasTemporGlass = true;
    }

    getCost(): number {
        return this.decoratedPhone.getCost() + 100;
    }

}

let myPhone: BasePhone = new IPhone();
console.log(myPhone.getDescription());
console.log(myPhone.getCost());

myPhone = new PhoneWithMemoryCard(myPhone);
console.log(myPhone.getDescription());
console.log(myPhone.getCost());

myPhone = new PhoneWithTemporGlass(myPhone);
console.log(myPhone.getDescription());
console.log(myPhone.getCost());