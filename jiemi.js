const CryptoJs = require('crypto-js')




function w(t) {
    var {SIGN: t, str: n} = t
        , n = (n = decodeURI(n),
        CryptoJs.HmacSHA1(CryptoJs.enc.Utf8.parse(n), t));
    t = CryptoJs.enc.Base64.stringify(n).toString();
    return CryptoJs.MD5(t).toString();
}


function main123(p){
    O = "D23ABC@#56"

    v = w({
        SIGN: O,
        str: p.replace(/^\/|https?:\/\/\/?/, "")
    })


    return v;
}


