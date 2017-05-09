package com.example.ottoniel.clientecalendar;

import android.app.ProgressDialog;
import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.NumberPicker;
import android.widget.Toast;

import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.Response;

import java.net.MalformedURLException;
import java.net.URL;

public class eventos extends AppCompatActivity {
    private String TAG = "Vik";
    ProgressDialog espera;
    public static OkHttpClient clienteWeb = new OkHttpClient();
    String salida="";
    String dia = "";
    String mes = "";
    String anio = "";
    String usuario = "";
    String evento = "";
    String descripcion = "";
    String hora = "";
    String lugar = "";
     //String[] mes = {"Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"};
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_eventos);
        usuario = getIntent().getStringExtra("usuario");
        final NumberPicker dias = (NumberPicker)findViewById(R.id.dias);
        final NumberPicker meses = (NumberPicker)findViewById(R.id.meses);
        final NumberPicker anios = (NumberPicker)findViewById(R.id.anio);
        Button b = (Button)findViewById(R.id.botonEvento);
        dias.setMinValue(1);
        dias.setMaxValue(31);
        anios.setMinValue(2017);
        anios.setMaxValue(3000);
        meses.setMinValue(1);
        meses.setMaxValue(12);
        //meses.setDisplayedValues(new String[]{"Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"});

        b.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                dia = String.valueOf(dias.getValue());
                mes = String.valueOf(meses.getValue());
                anio = String.valueOf(anios.getValue());
                EditText ev = (EditText)findViewById(R.id.cajaEvento);
                evento = ev.getText().toString();
                EditText lug = (EditText)findViewById(R.id.cajaLugar);
                lugar = lug.getText().toString();
                EditText des = (EditText)findViewById(R.id.cajaDescripcion);
                descripcion = des.getText().toString();
                EditText h = (EditText)findViewById(R.id.cajaHora);
                hora = h.getText().toString();
                if(ev.getText().toString().equals("")){
                    Toast.makeText(getApplicationContext(),"Llene el campo evento",Toast.LENGTH_LONG).show();
                    return;
                }
                if(h.getText().toString().equals("")){
                    Toast.makeText(getApplicationContext(),"Llene el campo hora",Toast.LENGTH_LONG).show();
                    return;
                }
                if(des.getText().toString().equals("")){
                    Toast.makeText(getApplicationContext(),"Llene el campo descripcion",Toast.LENGTH_LONG).show();
                    return;
                }
                if(lug.getText().toString().equals("")){
                    lugar = "---";
                }
                Conexion c = new Conexion();
                c.execute();

                try{
                    Thread.sleep(1000);

                }catch (Exception e){

                }
                if(salida.equals("si")){
                    Toast.makeText(getApplicationContext(),"Evento creado",Toast.LENGTH_LONG).show();
                }else{
                    Toast.makeText(getApplicationContext(),"Fallo del servidor",Toast.LENGTH_LONG).show();
                }
                ev.setText("");
                h.setText("");
                des.setText("");
                lug.setText("");


            }
        });

    }
    private class Conexion extends AsyncTask<Void, Void, Void> {
        @Override
        protected Void doInBackground(Void... params) {
            System.out.println("1---------------------------------------------------------------");
            Log.i("Vik", "doInBackground");
            //verificarLogin(usu,contra);
            crearEvento(usuario,evento,descripcion,lugar,hora,anio,mes,dia);
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
            espera = new ProgressDialog(eventos.this);
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
    private void crearEvento(String usuario, String evento, String descripcion, String lugar, String hora, String anio, String mes, String dia){
        try{
            System.out.println("2------------------------------------");
            URL url = new URL("http://192.168.1.11:8000/nuevoEvento?"+"usuario="+usuario+"&evento="+evento+"&descripcion="+descripcion
            +"&hora="+hora+"&lugar="+lugar+"&dia="+dia+"&mes="+mes+"&anio="+anio);
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
