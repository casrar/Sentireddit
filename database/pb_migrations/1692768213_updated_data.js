migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("9lgohp90l2nt12k")

  collection.deleteRule = ""

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("9lgohp90l2nt12k")

  collection.deleteRule = null

  return dao.saveCollection(collection)
})
