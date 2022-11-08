var aysnc  = require ("async")
function square(x) {
    console.log("here i come for promise");
    return new Promise ((resolve) => {
        setTimeout(() => {
            resolve(Math.pow(x,2));
        }, 1000);
    });
}

async function output(x) {
    console.log("Before display go promise");
    const ans = await square(x);
    console.log(ans);
}

output(10);