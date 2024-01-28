migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("1v6d2tdwyh005gp")

  collection.listRule = ""

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("1v6d2tdwyh005gp")

  collection.listRule = null

  return dao.saveCollection(collection)
})
