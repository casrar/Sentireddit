migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("js50r8yv2u12b4n")

  collection.deleteRule = ""

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("js50r8yv2u12b4n")

  collection.deleteRule = null

  return dao.saveCollection(collection)
})
