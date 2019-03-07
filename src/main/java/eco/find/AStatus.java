package eco.find;

import android.content.DialogInterface;
import android.content.Intent;
import android.support.annotation.NonNull;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.text.method.PasswordTransformationMethod;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.Spinner;
import android.widget.Toast;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

import java.util.ArrayList;

public class AStatus extends AppCompatActivity {
    public static String sp_value;
    ArrayList<String> ar = new ArrayList<String>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_astatus);




        Spinner spinner = (Spinner) findViewById(R.id.spinner1);
        Button getData = (Button) findViewById(R.id.getData);
        Button addData = (Button) findViewById(R.id.addData);

        ar.add("202481592591255");
        ArrayAdapter<String> adp2 = new ArrayAdapter<String>(this, android.R.layout.simple_spinner_item, ar);
        adp2.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinner.setAdapter(adp2);
        spinner.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> arg0, View arg1, int position, long id) {

                sp_value = ar.get(position);

            }

            @Override
            public void onNothingSelected(AdapterView<?> arg0) {
                // TODO Auto-generated method stub
            }
        });


        getData.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                    Intent intent = new Intent(AStatus.this, Status.class);
                    startActivity(intent);
            }
        });

        addData.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
              addValue();
            }
        });

      }

    private void addValue() {

        AlertDialog.Builder alertDialog = new AlertDialog.Builder(AStatus.this);
        alertDialog.setTitle("Add Device");
        final EditText macAddr = new EditText(AStatus.this);


        //macAddr.setTransformationMethod(PasswordTransformationMethod.getInstance());


        macAddr.setHint("Enter Device MAC Address");

        LinearLayout ll=new LinearLayout(AStatus.this);
        ll.setOrientation(LinearLayout.VERTICAL);

        ll.addView(macAddr);

        alertDialog.setView(ll);
        alertDialog.setPositiveButton("Add",
                new DialogInterface.OnClickListener() {
                    public void onClick(DialogInterface dialog, int id) {
                        add(macAddr.getText().toString());
                        dialog.cancel();
                    }
                });
        alertDialog.setNegativeButton("Cancel",
                new DialogInterface.OnClickListener() {
                    public void onClick(DialogInterface dialog, int id) {
                        dialog.cancel();
                    }
                });

        AlertDialog alert11 = alertDialog.create();
        alert11.show();
    }
    public void add(final String mac){

    ar.add(mac);
    Toast.makeText(AStatus.this,"new device added",Toast.LENGTH_LONG).show();

    }
}
