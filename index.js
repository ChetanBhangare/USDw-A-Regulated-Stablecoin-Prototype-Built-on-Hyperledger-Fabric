// chaincode/usdw/index.js
'use strict';

const USDwContract = require('./lib/usdwContract');

module.exports.USDwContract = USDwContract;
module.exports.contracts = [USDwContract];
