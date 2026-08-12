/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function(s, t) {
    let map = new Map();
    let used = new Set();

    for (let i = 0; i < s.length; i++) {
        let charS = s[i];
        let charT = t[i];

        if (map.has(charS)) {
            if (map.get(charS) !== charT) {
                return false;
            }
        } else {
            if (used.has(charT)) {
    return false;
    }

    map.set(charS, charT);
    used.add(charT);
}
}

    return true;
};