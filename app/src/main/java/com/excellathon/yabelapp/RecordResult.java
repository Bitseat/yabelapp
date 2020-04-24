package com.excellathon.yabelapp;

import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import java.io.FileInputStream;

public class RecordResult extends AppCompatActivity {
//    private ImageView imageViewer;
//    private GtsrbClassifier gtsrbClassifier;
//    private TextView tvClassified;
//    private Bitmap bmp = null;
//    private static final String TAG = "DetectLogo2";
    private TextView name;
    private TextView date;
    private TextView amount;
    private TextView amount_figure;
    private Button SaveToDB;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.office_form);
        String filename = getIntent().getStringExtra("content");
        name = (TextView) findViewById(R.id.nameTv);
        date = (TextView) findViewById(R.id.dateTv);
        name.setText("Hana sinishaw");
        date.setText(filename);

        //Button saveButton = (Button) findViewById(R.id.btnSv);
    }
}
