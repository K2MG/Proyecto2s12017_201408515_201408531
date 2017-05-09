package com.example.ottoniel.clientecalendar;

import android.app.ProgressDialog;
import android.content.Intent;
import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.Response;

import java.net.MalformedURLException;
import java.net.URL;

public class registrar extends AppCompatActivity {
    EditText usuario;
    EditText pass;
    String usu;
    String contra;
    private String TAG = "Vik";
    ProgressDialog espera;
    public static OkHttpClient clienteWeb = new OkHttpClient();
    String salida="";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_registrar);
        Button b = (Button)findViewById(R.id.botonRegistrar);
        usuario = (EditText)findViewById(R.id.cajaUsuario);
        pass = (EditText)findViewById(R.id.cajaPassword);

        b.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                usu = usuario.getText().toString();
                contra = pass.getText().toString();
                if(usuario.getText().equals("") || pass.getText().equals("")){
                    Toast.makeText(getApplicationContext(),"Llene todos los campos",Toast.LENGTH_LONG).show();
                    return;
                }
                if(pass.getText().length()<4){
                    Toast.makeText(getApplicationContext(),"La contraseña debe tener al menos 4 caracteres", Toast.LENGTH_LONG).show();
                    return;
                }
                Conexion c = new Conexion();
                c.execute();
                try{
                    Thread.sleep(1000);

                }catch (Exception e){

                }

                if(salida.equals("exito")){
                    Toast.makeText(getApplicationContext(),"Registrado exitosamente", Toast.LENGTH_LONG).show();
                    usuario.setText("");
                    pass.setText("");
                }else{
                    Toast.makeText(getApplicationContext(),"Usuario ya existe ingrese otro",Toast.LENGTH_LONG).show();
                }
            }
        });
    }
    private class Conexion extends AsyncTask<Void, Void, Void> {
        @Override
        protected Void doInBackground(Void... params) {
            System.out.println("1---------------------------------------------------------------");
            Log.i("Vik", "doInBackground");
            //verificarLogin(usu,contra);
            registrar(usu,contra);
            return null;
        }

        @Override
        protected void onPostExecute(Void result) {
            Log.i("Vik", "onPostExecute");

            espera.dismiss();
        }


        @Override
        protected void onPreExecute() {
            Log.i("Vik", "onPreExecute");
            super.onPreExecute();
            espera = new ProgressDialog(registrar.this);
            espera.setMessage("Cargando...");
            espera.setIndeterminate(false);
            espera.setProgressStyle(ProgressDialog.STYLE_SPINNER);
            espera.setCancelable(true);
            espera.show();
        }

        @Override
        protected void onProgressUpdate(Void... values) {
            Log.i("Vik", "onProgressUpdate");
        }
    }
    private void registrar(String usuario, String contrasenia){
        try{
            System.out.println("2------------------------------------");
            URL url = new URL("http://192.168.1.11:8000/insertarUsuario?"+"usuario="+usuario+"&password="+contrasenia);
            Request req = new Request.Builder().url(url).get().build();
            System.out.println("3------------------------------------------------");
            Response resp = clienteWeb.newCall(req).execute();
            salida = resp.body().string();
            System.out.println("4-----------------------------------------"+salida);

        } catch(MalformedURLException ex){
            System.out.println(ex.toString());
        }catch(Exception ex){
            System.out.println(ex.toString());
        }
    }
}
