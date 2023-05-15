/**
 * @param {number} millis
 */
async function sleep(millis) {
    function callback(res,rej){
        setTimeout(res,millis)
    }
    return new Promise(callback)
}

/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */