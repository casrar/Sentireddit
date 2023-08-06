migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("js50r8yv2u12b4n")

  collection.createRule = ""

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("js50r8yv2u12b4n")

  collection.createRule = null

  return dao.saveCollection(collection)
})
