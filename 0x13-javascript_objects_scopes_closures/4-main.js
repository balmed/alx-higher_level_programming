#!/usr/bin/node
const Rectangle =3D require('./4-rectangle');

const r1 =3D new Rectangle(2, 3);
console.log('Normal:');
r1.print();

console.log('Double:');
r1.double();
r1.print();

console.log('Rotate:');
r1.rotate();
r1.print();
