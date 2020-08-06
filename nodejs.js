// const main = () => {
//   console.log('print1');

//   //call stack->web api -> exceutes -> pass to event queue -> once call stack gets empty this function gets executed
//   setTimeout(() => {
//     console.log('callback');
//   }, 0);
//   console.log('print2');
// };

// main();

//how to use promises
a = 1;
b = '1';
console.log(b == a);

console.log('first');

const doSomething = () => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      console.log('function exected after 1 s');
      resolve('data');
    }, 1000);
  });
};

doSomething()
  .then((data) => {
    console.log(data);
    // throw Error('something went worng');
    return new Promise((resolve) => {
      resolve(data + '1');
    });
  })
  .then((data1) => {
    console.log(data1);
  })
  .catch((e) => {
    console.log(e);
  });

console.log('last');
