# Understanding Chaincode

Lets start with a simple chaincode to ensure we understand the basic concepts.

We will use a simple Land Record(landrec) chaincode which will do CRUD operations on basic land records.

We will be using javascript(node) as the language for our chaincode. GO is also supported though.

We will use the `fabric-contract-api` node package to write our chaincode.

### How chaincode works

Chaincode application is simple. It stores and retrieves data from underlying world-state databases and can hold any logic. Since couch db is a key-value based db, it is quite simple. Based on the data it changes in the world-state the fabric peer itself generates the transaction with “changed” data.

The `fabric-contract-api` requires our chaincode class to extend the `Contract` class.

- The `async initLedger(ctx)` method is called whenever a chaincode is initialized.

- We can add more methods depending on what functionality we want our chaincode to expose. There are a couple of important methods passed in context object that allow us to store and retrieve data from the key value store.

Look at the sample code below. There are two functions supported by this chaincode. CreateLand and QueryLand. Once this chaincode is deployed, any application can call these methods given that it calls it signed with a valid user’s private key whose certificate is issued by our CA. Important lines are highlighted

```js
"use strict";

const { Contract } = require("fabric-contract-api");

class LandRec extends Contract {
  async initLedger(ctx) {
    console.info("============= START : Initialize Ledger ===========");
    // todo
    console.info("============= END : Initialize Ledger ===========");
  }

  async queryLand(ctx, landNumber) {
    const landAsBytes = await ctx.stub.getState(landNumber); // get the land from chaincode state
    if (!landAsBytes || landAsBytes.length === 0) {
      throw new Error(`${landNumber} does not exist`);
    }
    console.log(landAsBytes.toString());
    return landAsBytes.toString();
  }

  async createLand(ctx, landNumber, address, location, owner) {
    console.info("============= START : Create Land ===========");

    const land = {
      docType: "land",
      address,
      location,
      owner,
    };

    await ctx.stub.putState(landNumber, Buffer.from(JSON.stringify(land)));
    console.info("============= END : Create Land ===========");
  }
}
```

# Deploy your Chaincode

## Folder Structure for `Chaincode` Folder

---

Please note that infra-basic-network has all the stuff we used earlier to bring up a network. We will use the same network now and deploy our landrec chaincode on it.

Now lets look at important files inside the `chaincode` folder.

1. `lib/landrec.js:` This contains the chaincode logic which reads and writes values to key value-based data store (state db). This defines valid transactions on the ledger.

2. `index.js:` This is used to expose the landrec chaincode module.

3. `docker-compose.yml:` This defines the fabric-tools container from which we will deploy our chaincode. This container will access the chaincode as mounted volume and will connect to same docker network as our fabric network components.

### Running the Environment

#### 1. Run Fabric Network#

```bash
cd /usercode/infra-basic-network && ./exercise-1.sh
```

#### 2. Launch Tools Container

Docker compose command to bring up the tools container.

```bash
cd /usercode/chaincode && docker-compose up -d cli
```

#### 3. Install chaincode

```bash
docker exec -e "CORE_PEER_LOCALMSPID=Org1MSP" \
            -e "CORE_PEER_MSPCONFIGPATH=/opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/org1.example.com/users/Admin@org1.example.com/msp" \
       cli peer chaincode install \
            -n landrec \
            -v 1.0 \
            -p "/opt/gopath/src/github.com" \
            -l "node"
```

#### 4. Instantiate chaincode

```bash
docker exec -e "CORE_PEER_LOCALMSPID=Org1MSP" \
            -e "CORE_PEER_MSPCONFIGPATH=/opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/org1.example.com/users/Admin@org1.example.com/msp" \
       cli peer chaincode instantiate \
            -o orderer.example.com:7050 \
            -C mychannel \
            -n landrec \
            -l "node" \
            -v 1.0 \
            -c '{"Args":[]}' \
            -P "OR ('Org1MSP.member','Org2MSP.member')"
```

#### 5. Test chaincode invoke

```bash
docker exec -e "CORE_PEER_LOCALMSPID=Org1MSP" \
            -e "CORE_PEER_MSPCONFIGPATH=/opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/org1.example.com/users/Admin@org1.example.com/msp" \
       cli peer chaincode invoke \
            -o orderer.example.com:7050 \
            -C mychannel \
            -n landrec \
            -c '{"function":"initLedger","Args":[]}'
```
