// This tests the creation of a resource that contains "simple" input and output propeprties.
// In particular, there aren't any fancy dataflow linked properties.

let assert = require("assert");
let fabric = require("../../../../lib");

class MyResource extends fabric.Resource {
    constructor(name) {
        super("test:index:MyResource", name, {
            // First a few basic properties that are resolved to values.
            "inpropB1": new fabric.Property(false),
            "inpropB2": new fabric.Property(true),
            "inpropN": new fabric.Property(42),
            "inpropS": new fabric.Property("a string"),
            "inpropA": new fabric.Property([ true, 99, "what a great property" ]),
            "inpropO": new fabric.Property({
                b1: false,
                b2: true,
                n: 42,
                s: "another string",
                a: [ 66, false, "strings galore" ],
                o: { z: "x" },
            }),

            // Next some properties that are completely unresolved (outputs).
            "outprop1": new fabric.Property(),
            "outprop2": new fabric.Property(),
        });
    }
}

let res = new MyResource("testResource1");
res.id.then(id => {
    console.log(`ID: ${id}`);
    assert.equal(id, "testResource1");
});
res.urn.then(urn => {
    console.log(`URN: ${urn}`);
    assert.equal(urn, "test:index:MyResource::testResource1");
});
res.outprop1.then(prop => {
    console.log(`OutProp1: ${prop}`);
    assert.equal(prop, "output properties ftw");
});
res.outprop2.then(prop => {
    console.log(`OutProp2: ${prop}`);
    assert.equal(prop, 998.6);
});

