from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI
import pandas as pd

DATABASE_URL_ORIGIN = "postgresql://admin:postgres@host.docker.internal:5433/postgres"
DATABASE_URL_DESTINATION = "postgresql://admin:postgres@host.docker.internal:5434/postgres"

engine_origin = create_engine(DATABASE_URL_ORIGIN)
SessionLocal_origin = sessionmaker(autocommit=False, autoflush=False, bind=engine_origin)

engine_destination = create_engine(DATABASE_URL_DESTINATION)
SessionLocal_destination = sessionmaker(autocommit=False, autoflush=False, bind=engine_destination)


app = FastAPI()


@app.get("/migrate-data/")
def migrate_data():
    # Crear sesión para la base de datos origen
    session_origin = SessionLocal_origin()
    # Crear sesión para la base de datos destino
    session_destination = SessionLocal_destination()
    
    try:
        # Leer todos los datos de origen
        with session_origin.connection() as connection:
            # Ejecutar la consulta
            result = connection.execute(text("select * from ejemplo"))
            df = pd.DataFrame(result, columns=result.keys())
        print(df)
        with session_destination.connection() as connection:
            df.to_sql('destination', con=connection, if_exists='append', index=False)
            connection.commit()
        return {"status": "success", "message": "Data migrated successfully."}
    except Exception as e:
        session_destination.rollback()
        return {"status": "error", "message": str(e)}
    finally:
        session_origin.close()
        session_destination.close()