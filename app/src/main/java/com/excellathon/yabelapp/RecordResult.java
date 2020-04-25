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

import com.chaquo.python.PyObject;
import com.chaquo.python.Python;
import com.chaquo.python.android.AndroidPlatform;

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

        if (! Python.isStarted()) {
            Python.start(new AndroidPlatform(this));
        }

        Python py = Python.getInstance();
        PyObject pyf = py.getModule("ocr_preprocess");

        PyObject obj = pyf.callAttr("test", filename);

        name = (TextView) findViewById(R.id.payto);
        date = (TextView) findViewById(R.id.date);
        amount = (TextView) findViewById(R.id.amount);
        amount_figure = (TextView) findViewById(R.id.amount_figure);
        name.setText(obj.asList().get(0).toString());
        date.setText(obj.asList().get(1).toString());
        amount.setText(obj.asList().get(2).toString());
        amount_figure.setText(obj.asList().get(3).toString());

        //Button saveButton = (Button) findViewById(R.id.btnSv);
    }
}
