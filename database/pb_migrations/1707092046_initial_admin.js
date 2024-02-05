migrate((db) => {
  const dao = new Dao(db)

  const admin = new Admin()
  admin.email = $os.getenv("DB_IDENTITY")
  admin.setPassword($os.getenv("DB_PASSWORD"))
  
  dao.saveAdmin(admin)

}, (db) => {
  const dao = new Dao(db)
  try {
    const admin = dao.findAdminByEmail($os.getenv("DB_IDENTITY"))

    dao.deleteAdmin(admin)
  } catch (_) {
    // Admin likely deleted already 
    // https://pocketbase.io/docs/js-migrations/#creating-new-admin
  }
})
