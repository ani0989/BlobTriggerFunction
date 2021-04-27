module.exports = async function (context, myBlob, req) {
    context.log('JavaScript Blob trigger function processed a request.');
    // You can call and await an async method here
    return context.bindings.myBlob.toString()
}