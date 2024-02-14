#!/usr/bin/node
const converter =3D require('./10-converter').converter;

let myConverter =3D converter(10);

console.log(myConverter(2));
console.log(myConverter(12));
console.log(myConverter(89));


myConverter =3D converter(16);

console.log(myConverter(2));
console.log(myConverter(12));
console.log(myConverter(89));
