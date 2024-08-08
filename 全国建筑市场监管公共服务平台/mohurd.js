const CryptoJS = require("crypto-js");

var f = CryptoJS.enc.Utf8.parse("Dt8j9wGw%6HbxfFn");
var m = CryptoJS.enc.Utf8.parse("0123456789ABCDEF");
function b(t) {
  var e = CryptoJS.enc.Hex.parse(t),
    n = CryptoJS.enc.Base64.stringify(e);
  console.log(n);

  var a = CryptoJS.AES.decrypt(n, f, {
      iv: m,
      mode: CryptoJS.mode.CBC,
      padding: CryptoJS.pad.Pkcs7,
    }),
    r = a.toString(CryptoJS.enc.Utf8);
  return r.toString();
}
