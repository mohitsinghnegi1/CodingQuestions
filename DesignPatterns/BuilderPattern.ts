// This design pattern we use when there are some optional and some required attributes , instead of passing undefined we can use this pattern

// Traditional way of implimenting this pattern

class Address {
    houseNo: number;
    city: string;
    state: string;
    constructor(houseNo: number, city: string, state: string) {
        this.houseNo = houseNo;
        this.city = city;
        this.state = state;
    }
}
class Employee {
    name: string;
    age?: number;
    address?: Address;
    constructor(name: string) {
        this.name = name;
    }

    setAge(age: number) {
        this.age = age;
        return this;
    }

    setAddress(address: Address): Employee {
        this.address = address;
        return this;
    }


}


class EmployeeBuilder {
    employee: Employee;
    constructor(name: string) {
        this.employee = new Employee(name);
    }

    setAge(age: number): EmployeeBuilder {
        this.employee.age = age;
        return this;
    }

    setAddress(address: Address): EmployeeBuilder {
        this.employee.address = address;
        return this;
    }

    build() {
        return this.employee;
    }
}

let employee: Employee = new EmployeeBuilder('mohit').setAddress(new Address(2, 'dehradun', 'uttarakhand')).setAge(22).build();
console.log(employee);

let employee2: Employee = new EmployeeBuilder('vaibhav').setAge(22).build();
console.log(employee2);



// Javascript way of implementing builder pattern

type options = {
    age?: number,
    address?: Address;
};

class Person {
    name: string;
    age: number | undefined;
    address: Address | undefined;
    constructor(name: string, { age = undefined, address }: options = {}) {
        this.name = name;
        this.age = age;
        this.address = address;
    }
}

let person1 = new Person('mohit', { age: 20, address: new Address(10, 'dehradun', 'uttarakhand') });
console.log(person1);

let person2 = new Person('vaibhav', { address: new Address(10, 'dehradun', 'uttarakhand') });
console.log(person2);