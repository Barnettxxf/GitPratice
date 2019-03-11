function outer() {
    var result = [];
    for (var i = 0; i < 10; i++) {
        result[i] = function () {
            console.log(i)
        }
    }

}

inner = outer();
inner.forEach(function (e, i, a) {
    e();
});

function outer_one() {
    var result = [];
    for (var i = 0; i < 10; i++) {
        result[i] = function (num) {
            return function () {
                console.log(num)
            }
        }(i)
    }

}

console.log('========================');

inner_one = outer_one();



function outer_two() {
    var result = [];
    var inner = function (num) {
        console.log(num)
    };
    for (var i = 0; i < 10; i++) {
        result[i] = inner(i)
    }
    return result;
}

console.log('========================');

outer_two = outer_two();
outer_two.forEach(function (e, i, a) {

});