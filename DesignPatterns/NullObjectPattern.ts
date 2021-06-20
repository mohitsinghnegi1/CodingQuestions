class User {
    name: string;
    id: string;
    constructor(name: string, id: string) {
        this.name = name;
        this.id = id;
    }
}

class NullUser {
    name: string;
    id: string;
    constructor() {
        this.name = "Guest";
        this.id = "-";
    }
}

let users = [
    new User('mohit', 'id-1'),
    new User('Vaibhav', 'id-2')
];

const findUser = (userName: string) => {
    let user: User | undefined = users.find((user) => user.name == userName);
    if (user) return user;
    return new NullUser();
};


let user = findUser('mohit');
console.log(`Valid user:: User name ${ user.name } and user id ${ user.id }`);

user = findUser('Mannu');
console.log(`Invalid user:: User name ${ user.name } and user id ${ user.id }`);
