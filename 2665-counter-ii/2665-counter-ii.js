/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    ans=init
    function increment(){
        return ++ans
    }
    function reset(){
        return ans=init
    }
    function decrement(){
        return --ans
    }
    return {increment,reset,decrement}
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */