try{
    fuck.shit("fuck");
}catch(e){
    // console.dir(e);
    console.log(Object.getOwnPropertyNames(e));
    ["stack","message"]
    console.log(Object.getOwnPropertyNames(Object.getPrototypeOf(e)));
    ["name","message","toString"]
    console.log(Object.getOwnPropertyNames(Object.getPrototypeOf(Object.getPrototypeOf(e))));
    var message = e["message"]
    // console.log(message) // fuck is not defined.
    // console.log(typeof(e.stack)) // still string. just combine them?
process.stderr.write(e.message+"\n"+e.stack)
}