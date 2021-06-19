interface State {
    order: Order;
    verifyPayment(): boolean; // transition functions
    cancelOrder(): boolean;
    shipOrder(): boolean;
}

class PaymentPending implements State {
    order: Order;

    constructor(order: Order) {
        this.order = order;
    }
    verifyPayment(): boolean {
        console.log('Payment is being verified');
        this.order.setState(this.order.orderBeingPrepared);
        return true;
    }
    cancelOrder(): boolean {
        console.log('Order is being cancelled');
        this.order.setState(this.order.orderCancelled);
        return true;
    }
    shipOrder(): boolean {
        console.log('Cannot ship order before Payment verified');
        return false;
    }

}

class OrderCancelled implements State {
    order: Order;

    constructor(order: Order) {
        this.order = order;
    }
    verifyPayment(): boolean {
        console.log('Payment could not be varified after order cancellation ');
        return false;
    }
    cancelOrder(): boolean {
        console.log('Order is already cancelled');
        return true;
    }
    shipOrder(): boolean {
        console.log('Could not ship cancelled order');
        return false;
    }

}


class OrderBeingprepared implements State {
    order: Order;

    constructor(order: Order) {
        this.order = order;
    }
    verifyPayment(): boolean {
        console.log('Payment is already verified');
        return false;
    }
    cancelOrder(): boolean {
        console.log('Order is being cancelled');
        this.order.setState(this.order.orderCancelled);
        return true;
    }
    shipOrder(): boolean {
        console.log('Order is being Shipped');
        this.order.setState(this.order.orderShipped);
        return true;
    }

}

class OrderShipped implements State {
    order: Order;

    constructor(order: Order) {
        this.order = order;
    }
    verifyPayment(): boolean {
        console.log('Payment is already being verified');
        return false;
    }
    cancelOrder(): boolean {
        console.log('Order could not be canelled after shipment');
        return false;
    }
    shipOrder(): boolean {
        console.log('Order is already Shipped');
        return false;
    }
}




class Order {
    private state: State;
    public paymentPending: PaymentPending;
    public orderCancelled: OrderCancelled;
    public orderBeingPrepared: OrderBeingprepared;
    public orderShipped: OrderShipped;

    constructor() {
        this.paymentPending = new PaymentPending(this);
        this.orderCancelled = new OrderCancelled(this);
        this.orderBeingPrepared = new OrderBeingprepared(this);
        this.orderShipped = new OrderShipped(this);
        this.state = this.paymentPending;
    }

    setState(state: State) {
        this.state = state;
    }

    getState() {
        return this.state;
    }

}

let order = new Order();
order.getState().verifyPayment();
// order.getState().cancelOrder();
order.getState().verifyPayment();
order.getState().shipOrder();

console.log((<any>order.getState()).constructor.name);