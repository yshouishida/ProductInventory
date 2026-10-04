using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Text.Json;
using System.Net.Http;
using System.Threading.Tasks;
using System.Windows.Forms;
using prjProductInventory.Models;

namespace prjProductInventory
{
    public partial class frmMain : Form
    {
        private readonly HttpClient client = new HttpClient();
        private const string BASE_URL = "http://127.0.0.1:5000/products";

        public frmMain()
        {
            InitializeComponent();
        }

        private async Task LoadProducts()
        {
            try
            {
                HttpResponseMessage response = await client.GetAsync(BASE_URL);
                string json = await response.Content.ReadAsStringAsync();

                if (response.IsSuccessStatusCode)
                {
                    ApiResponse<List<Product>> result = JsonSerializer.Deserialize <ApiResponse<List<Product>>>(json);

                    dgvProducts.DataSource = result.data;

                    dgvProducts.Columns["id"].Visible = false;

                    dgvProducts.ClearSelection();
                    dgvProducts.CurrentCell = null;
                    dgvProducts.AutoGenerateColumns = false;
                }
                else
                {
                    ApiResponse<object> message = JsonSerializer.Deserialize<ApiResponse<object>>(json);
                    MessageBox.Show(message.ToString(), "Error");
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        private void btnNew_Click(object sender, EventArgs e)
        {

        }

        private void btnEdit_Click(object sender, EventArgs e)
        {

        }

        private async void btnDelete_Click(object sender, EventArgs e)
        {

            if (dgvProducts.CurrentRow == null)
            {
                MessageBox.Show("Please select a record to delete.");
                return;
            }

            if (MessageBox.Show(
                "Do you want to delete this product?", 
                "Delete confirmation", 
                MessageBoxButtons.YesNo,
                MessageBoxIcon.Exclamation
                ) == DialogResult.No) return;

            int productId = Convert.ToInt32(dgvProducts.CurrentRow.Cells["id"].Value);

            try
            {
                HttpResponseMessage response = await client.DeleteAsync($"{BASE_URL}/{productId}");
                string json = await response.Content.ReadAsStringAsync();
                
                if (response.IsSuccessStatusCode)
                {
                    ApiResponse<object> message = JsonSerializer.Deserialize<ApiResponse<object>>(json);
                    MessageBox.Show(message.message.ToString(), "Message", MessageBoxButtons.OK, MessageBoxIcon.Information);
                    await LoadProducts();
                }
                else
                {
                    ApiResponse<object> message = JsonSerializer.Deserialize<ApiResponse<object>>(json);
                    MessageBox.Show(message.ToString(), "Error");
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }


        }

        private async void btnRefresh_Click(object sender, EventArgs e)
        {
            await LoadProducts();
        }

        private async void frmMain_Load(object sender, EventArgs e)
        {
            await LoadProducts();
        }

        private void dgvProducts_KeyDown(object sender, KeyEventArgs e)
        { 
            if (e.KeyCode == Keys.Delete)
            {
                btnDelete.PerformClick();
            }
        }

 
    }
}
