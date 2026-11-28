module.exports = process.env.DATABASE_URL && process.env.STORE !== 'memory' ? require('./store-pg') : require('./store-memory');
