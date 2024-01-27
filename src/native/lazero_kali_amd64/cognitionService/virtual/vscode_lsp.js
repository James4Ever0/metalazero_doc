const LSP = require("vscode-languageserver");
const connection = LSP.createConnection(new LSP.StreamMessageReader(process.stdin), new LSP.StreamMessageWriter(process.stdout));

//console.dir(connection)
connection.onInitialize((params) => __awaiter(this, void 0, void 0, function* () {console.log("initialized program")
        connection.console.log(`Initialized server v. 9999 for ${params.rootUri}`);
        const server = yield server_1.default.initialize(connection, params);
        server.register(connection);
        return {
            capabilities: server.capabilities(),
        };
    }));
connection.listen();
console.log("not blocking?")
// this is coming right from the process.
//sure thing. so we need to handle the initialization.
