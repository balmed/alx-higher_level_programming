#!/usr/bin/node
const Rectangle =3D require('./1-rectangle');

const r1 =3D new Rectangle(2, 3);
console.log(r1);
console.log(r1.width);
console.log(r1.height);

const r2 =3D new Rectangle(2, -3);
console.log(r2);
console.log(r2.width);
console.log(r2.height);

const r3 =3D new Rectangle(2);
console.log(r3);
console.log(r3.width);
console.log(r3.height);
